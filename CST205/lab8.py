def increaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*2)
  writeSoundTo(sound, "C://Developing//School//CST205//increaseVol.wav")
    
# Before 10730: 97, 20350: -33
# After  10730: -62, 20350: -66

def decreaseVolume(sound):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*0.5)
  writeSoundTo(sound, "C://Developing//School//CST205//decreaseVol.wav")
  
def changeVolume(sound, factor):
  for sample in getSamples(sound):
    value = getSampleValue(sample)
    setSampleValue(sample, value*factor)
  writeSoundTo(sound, "C://Developing//School//CST205//decreaseVol.wav")
  
def maxSample(sound):
  max_val = 0
  for sample in getSamples(sound):
    max_val = max(max_val, getSampleValue(sample))
  return max_val
    