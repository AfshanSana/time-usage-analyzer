import sys
from time_usage_analyzer.analyzer import (
    load_data,
    validate_data,
    analyze_time,
    daily_breakdown,
    give_suggestions,
    plot_time_usage,
)


def main():
    if len(sys.argv) < 2:
        print("Usage: python -m time_usage_analyzer <csv_file>")
        return

    file_path = sys.argv[1]

    try:
        df = load_data(file_path)
        validate_data(df)

        summary, total_hours = analyze_time(df)

        print("\nTime Usage Summary:")
        print(summary)

        print(f"\nTotal Hours: {total_hours}")

        # ⭐ NEW FEATURE
        daily = daily_breakdown(df)
        if daily is not None:
            print("\nDay-wise Breakdown:")
            print(daily)

        give_suggestions(summary)
        plot_time_usage(summary)

    except FileNotFoundError:
        print("Error: file not found.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()