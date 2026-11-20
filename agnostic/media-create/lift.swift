// Apple Vision subject lift: writes a greyscale mask of the foreground subject(s) in an image. On-device, no generation.
// usage: swift lift.swift <in.png> <out-mask.png> [group]
import Foundation
import Vision
import CoreImage
import ImageIO
import UniformTypeIdentifiers

let args = CommandLine.arguments
guard args.count == 3 || (args.count == 4 && ["group", "all"].contains(args[3])) else { print("usage: lift <in> <out-mask.png> [group|all]"); exit(2) }
let group = args.count == 4 && args[3] == "group"  // every instance with a real share of the crop's centre (a pair at play)
let all = args.count == 4 && args[3] == "all"      // every instance in the crop (a line of players)
let url = URL(fileURLWithPath: args[1])
guard let src = CGImageSourceCreateWithURL(url as CFURL, nil),
      let cg = CGImageSourceCreateImageAtIndex(src, 0, nil) else { print("cannot read image"); exit(1) }
let handler = VNImageRequestHandler(cgImage: cg, options: [:])
let req = VNGenerateForegroundInstanceMaskRequest()
do { try handler.perform([req]) } catch { print("vision failed: \(error)"); exit(1) }
guard let res = req.results?.first else { print("no subject"); exit(3) }
// Keep only the instance under the centre of the crop, since the crop is centred on one detected figure.
let inst = res.allInstances
let labels = res.instanceMask
CVPixelBufferLockBaseAddress(labels, .readOnly)
let w = CVPixelBufferGetWidth(labels), h = CVPixelBufferGetHeight(labels), row = CVPixelBufferGetBytesPerRow(labels)
let base = CVPixelBufferGetBaseAddress(labels)!.assumingMemoryBound(to: UInt8.self)
var counts = [Int](repeating: 0, count: 256)
for y in (h * 3 / 10)..<(h * 7 / 10) { for x in (w * 35 / 100)..<(w * 65 / 100) { counts[Int(base[y * row + x])] += 1 } }
CVPixelBufferUnlockBaseAddress(labels, .readOnly)
counts[0] = 0
let best = counts.firstIndex(of: counts.max()!)!
var pick: IndexSet = best > 0 && inst.contains(best) ? IndexSet(integer: best) : inst
if group && best > 0 { pick = IndexSet(inst.filter { counts[$0] * 5 >= counts[best] }) }
if all { pick = inst }
do {
    let mask = try res.generateScaledMaskForImage(forInstances: pick, from: handler)
    let ci = CIImage(cvPixelBuffer: mask)
    let ctx = CIContext()
    let out = URL(fileURLWithPath: args[2])
    try ctx.writePNGRepresentation(of: ci, to: out, format: .L8, colorSpace: CGColorSpaceCreateDeviceGray())
    print("ok instances=\(inst.count) picked=\(Array(pick))")
} catch { print("mask failed: \(error)"); exit(1) }
