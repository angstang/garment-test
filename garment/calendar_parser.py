import requests
from icalendar import Calendar
from typing import Optional
import sys

CALENDAR_URL = "https://mail.aidi.edu.cn/viewsharecalendar.php?userid=xueliling@nitbj.com&usercode=a0adf814d81385fffabcfcb7bae1224e&opt=month"
TIMEOUT = 10


def fetch_calendar(url: str) -> Optional[Calendar]:
    """获取远程日历数据"""
    try:
        response = requests.get(url, timeout=TIMEOUT)
        response.raise_for_status()
        return Calendar.from_ical(response.text)
    except requests.RequestException as e:
        print(f"错误：无法获取日历数据 - {e}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"错误：日历解析失败 - {e}", file=sys.stderr)
        return None


def parse_events(calendar: Calendar) -> None:
    """解析并输出日历事件"""
    event_count = 0
    for component in calendar.walk():
        if component.name == "VEVENT":
            summary = component.get('summary', '无标题')
            dtstart = component.get('dtstart')
            dtend = component.get('dtend')
            description = component.get('description', '无描述')

            if dtstart is None:
                continue

            start_time = dtstart.dt
            end_time = dtend.dt if dtend else '未设定'

            print(f"事件: {summary}")
            print(f"开始时间: {start_time}")
            print(f"结束时间: {end_time}")
            print(f"描述: {description}")
            print("-" * 40)
            event_count += 1

    print(f"\n共找到 {event_count} 个事件")


def main():
    """主程序"""
    calendar = fetch_calendar(CALENDAR_URL)
    if calendar:
        parse_events(calendar)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()