"""Compatibility entry point for the separated Task-029-B pipeline."""
from solver.run_all import main as run_all
from processing.build_processed_data import main as process_all
from export.export_origin import main as export_all
from plotting.generate_figures import main as plot_all


def main():
    run_all()
    process_all()
    export_all()
    plot_all()


if __name__ == "__main__":
    main()
