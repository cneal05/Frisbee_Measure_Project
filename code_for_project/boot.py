# type: ignore
import board
import digitalio
import storage

switch = digitalio.DigitalInOut(board.GP22)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP

if not switch.value:
    storage.remount("/", readonly=False)