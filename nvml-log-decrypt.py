#!/usr/bin/env python3
import sys

# example generating log file:
# __NVML_DBG_FILE=nvml-trace.log __NVML_DBG_LVL=DEBUG nvidia-smi -L

class XorWow:
  def __init__(self, counter, x):
    self.counter = counter
    self.x = x

  def generate(self):
    # https://en.wikipedia.org/wiki/Xorshift#xorwow
    s = self.x[0]
    t = self.x[4]
    self.x[4] = self.x[3]
    self.x[3] = self.x[2]
    self.x[2] = self.x[1]
    self.x[1] = s
    t = (t ^ (t >> 2)) & 0xFFFFFFFF
    t = (t ^ (t << 1)) & 0xFFFFFFFF
    t = (t ^ (s ^ (s << 4))) & 0xFFFFFFFF
    self.x[0] = t
    self.counter = (self.counter + 0x587c5) & 0xFFFFFFFF
    return (t + self.counter) & 0xFFFFFFFF

def main():
  if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <nvml_trace.log>")
    exit(1)

  dec_dat = b""
  xorwow = XorWow(0xe44a4f49, [0x7645f3ed, 0x23cc0ec3, 0xaa7b8e81, 0x1d4d4848, 0xd3daecb8])
  with open(sys.argv[1], "rb") as f:
    for b in f.read():
      c = xorwow.generate() & 0xFF
      dec_dat += bytes([(b - c) & 0xFF])
  print(dec_dat.decode())

if __name__ == "__main__":
  main()
