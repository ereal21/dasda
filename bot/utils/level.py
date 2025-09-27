LEVEL_NAMES = [
    "Apartamentų lankytojas",
    "Apartamentų mėgėjas",
    "Apartamentų fanas",
    "Apartamentų liūtas",
    "Apartamentų vairuotojas",
    "Apartamentų apsauga",
    "Apartamentų VIP'as",
    "Apartamentų vadovas",
    "Apartamentų dešinė ranka",
    "Apartamentų valdžia",
]


def get_level_info(purchases: int):
    """Return level details for given purchase count.

    Returns tuple of (level_name, discount_percent, progress_bar, battery_emoji).
    """
    if purchases < 0:
        purchases = 0
    # determine level index (0-9)
    level_index = min(purchases // 10, len(LEVEL_NAMES) - 1)
    level_name = LEVEL_NAMES[level_index]
    # Level 0 receives no discount; each subsequent level adds 1.2%
    discount = round(level_index * 1.2, 1)
    progress = purchases % 10
    segment = progress // 5  # 0 or 1
    battery = "🪫" if segment == 0 else "🔋"
    bars_filled = progress % 5
    progress_bar = "🟩" * bars_filled + "⬜️" * (5 - bars_filled)
    return level_name, discount, progress_bar, battery
