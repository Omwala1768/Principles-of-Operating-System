from multiprocessing import Process, Semaphore, Lock, Array, Value
import time
import random

BUFFER_LIMIT = 5
TOTAL_ITEMS = 10


def produce_items(shared_buffer, write_pos, read_pos, empty_slots, filled_slots, buffer_lock):
    print("[Producer] Process started", flush=True)

    for _ in range(TOTAL_ITEMS):
        value = random.randint(1, 100)

        empty_slots.acquire()
        buffer_lock.acquire()

        position = write_pos.value
        shared_buffer[position] = value

        print(f"[Producer] Produced item {value} at index {position}", flush=True)

        write_pos.value = (position + 1) % BUFFER_LIMIT

        buffer_lock.release()
        filled_slots.release()

        time.sleep(random.uniform(0.1, 0.3))


def consume_items(shared_buffer, write_pos, read_pos, empty_slots, filled_slots, buffer_lock):
    print("[Consumer] Process started", flush=True)

    for _ in range(TOTAL_ITEMS):
        filled_slots.acquire()
        buffer_lock.acquire()

        position = read_pos.value
        value = shared_buffer[position]

        print(f"[Consumer] Consumed item {value} from index {position}", flush=True)

        read_pos.value = (position + 1) % BUFFER_LIMIT

        buffer_lock.release()
        empty_slots.release()

        time.sleep(random.uniform(0.1, 0.3))


def run_program():
    print("Om Wala F119")
    print("Starting Producer and Consumer Processes...\n", flush=True)

    shared_buffer = Array('i', BUFFER_LIMIT)

    write_position = Value('i', 0)
    read_position = Value('i', 0)

    empty_slots = Semaphore(BUFFER_LIMIT)
    filled_slots = Semaphore(0)
    buffer_lock = Lock()

    producer_process = Process(
        target=produce_items,
        args=(
            shared_buffer,
            write_position,
            read_position,
            empty_slots,
            filled_slots,
            buffer_lock,
        ),
    )

    consumer_process = Process(
        target=consume_items,
        args=(
            shared_buffer,
            write_position,
            read_position,
            empty_slots,
            filled_slots,
            buffer_lock,
        ),
    )

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("\nProducer and Consumer processes have finished.")


if __name__ == "__main__":
    run_program()
