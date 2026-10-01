import sched, time

s = sched.scheduler(time.time, time.sleep)

print(len(s.queue))

def say(text):
    print(F"[{time.strftime('%H:%M:%S')}] {text}")

start = time.time()
print("Старт. Отсчет времени от t0 = 0\n")

s.enter(2, 1, say, ("Прошло 2 секунды (приоритет 1)",))
s.enter(2, 0, say, ("Прошло 2 секунды (приоритет 0 - СРАБОТАЕТ ПЕРВЫМ)",))
s.enter(1, 0, say, ("Прошло 1 секунды",))
s.enterabs(start + 3, 1, say, ("Абсолютное время t0+3 c",))
s.enter(0.5, 0, say, ("Прошло 0.5 секунды",))

print("Очередь до run():", len(s.queue), "задач")
print("run() блокирует поток, пока все задачи не выполнятся:\n")
s.run()
print("\nГотово. Пустая очередь?", s.empty())