import logging
import signal
import threading
import time
from identify import identify
from interface2 import main as initialize_ui
import os

pid = os.getpid()

logger = logging.getLogger("tof-overlay")
logging.basicConfig(filename='errors.log', filemode='w', level=logging.ERROR)

detected_cd_list = []
detected_kb_list = []
cooldowns = {
    'Q': 0,
    'E': 0,
    'R': 0,
}

currentKeybind = {
    'active': None
}


def identify_weapon_cooldown_runner(run_event=None):
    try:
        while run_event.is_set():
            keybind, cooldown = identify()
            detected_cd_list.append(cooldown)
            detected_kb_list.append(keybind)

            currentKeybind['active'] = keybind

            long_cooldown = None
            detected_cd_list.clear()

            if (cooldown and cooldown >= 11 and cooldown <= 60):
                long_cooldown = cooldown

            # keybind != None because sometimes the cd number goes to another keybind when switching
            if (long_cooldown and keybind):
                cooldowns[keybind] = long_cooldown
    except Exception as e:
        logger.error(e)


# Reduces the cooldown by 1 every sec
def cooldowns_reducer_runner(run_event=None):
    try:
        while run_event.is_set():
            for keybind in cooldowns:
                if (cooldowns[keybind] == 0):
                    continue

                # Use value from scanner when keybind is same as current keybind
                if keybind == currentKeybind['active'] and cooldowns[keybind] > 11:
                    continue
                else:
                    cooldowns[keybind] -= 1

            time.sleep(1)
    except Exception as e:
        logger.error(e)


def interface_runner(run_event=None):
    while run_event.is_set():
        initialize_ui(pid, cooldowns)


def main():
    run_event = threading.Event()
    run_event.set()

    try:
        identify_weapon_cooldown_task = threading.Thread(
            target=identify_weapon_cooldown_runner, args=(run_event,))
        identify_weapon_cooldown_task.start()

        cooldowns_reducer_task = threading.Thread(
            target=cooldowns_reducer_runner, args=(run_event,))
        cooldowns_reducer_task.start()

        interface_task = threading.Thread(
            target=interface_runner, args=(run_event,))
        interface_task.start()

        while 1:
            time.sleep(.1)
    except KeyboardInterrupt:
        print("Closing threads")
    except Exception as e:
        logger.error(e)

    os.kill(pid, signal.SIGTERM)
    run_event.clear()
    identify_weapon_cooldown_task.join()
    cooldowns_reducer_task.join()
    interface_task.join()


if __name__ == '__main__':
    main()
