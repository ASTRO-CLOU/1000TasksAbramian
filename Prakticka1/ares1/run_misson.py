"""Запуск: python run_mission.py --days 6 --seed 42"""
import argparse, sched, time
from mission import delta_v, flight_time, fuel_needed, random_event

def build_parser():
    p = argparse.ArgumentParser(description="Симулятор межпланетной миссии")
    p.add_argument("--days",  type=int,   default=5,   help="длительность миссии, сут")
    p.add_argument("--seed",  type=int,   default=None, help="зерно ГСЧ")
    p.add_argument("--speed", type=float, default=0.2, help="секунд на 1 сутки")
    return p

def main():
    args = build_parser().parse_args()
    resource = 100
    s = sched.scheduler(time.time, time.sleep)

    def day_report(day):
        """Отчёт за сутки; при исчерпании ресурса отменяет все задачи."""
        nonlocal resource
        desc, delta = random_event(args.seed + day if args.seed is not None else None)
        resource = max(0, min(100, resource + delta))
        print(f"Сутки {day:>2} | {desc:<38s} {delta:+3d} | ресурс {resource:3d}% "
              f"{'#' * (resource // 5)}")
        if resource == 0:
            for ev in list(s.queue):
                s.cancel(ev)
            return
        if day < args.days:
            s.enter(args.speed, 1, day_report, (day + 1,))

    def starter_info():
        result = f'Характеристическая скорость (Циолковский): {delta_v(45000, 20000):.1f} м/c\n Топлива для dv = 4000 м/с при сухой массе 20 т: {int(fuel_needed(20000, 4000)):,} кг\n Время перелёта 78,340 тыс. км при a = 0.003 м/с^2: {int(flight_time(78340000, 0.003)):,} ч = {round(flight_time(78340000, 0.003) / 24)} сут'
        print("=" * 62)
        print(f"{'МИССИЯ «АРЕС-1»: Марс':^62}")
        print("=" * 62)
        print(result)
        print("-" * 62)

        t = time.time()
        s.enter(0, 1, day_report, (1,))
        s.run()

        sim = time.time() - t
        print("-" * 62)
        print(f"Миссия завершена. Итоговый ресурс: {resource}%. Реальное время симуляции: {sim:.1f} c")
    
    starter_info()

if __name__ == "__main__":
    main()
