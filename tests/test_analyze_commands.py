import os.path
from pathlib import Path
from unittest.mock import patch
import pytest
from importlib.machinery import SourceFileLoader

omniperf = SourceFileLoader("omniperf", "src/omniperf").load_module()

baseline_opts = ["omniperf", "analyze"]

@pytest.mark.misc
def test_valid_path():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            ["omniperf", "analyze", "--path", "tests/workloads/mixbench/mi100"],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            ["omniperf", "analyze", "--path", "tests/workloads/mixbench/mi200"],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.misc
def test_list_kernels():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--list-kernels",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--list-kernels",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.list_metrics
def test_list_metrics_gfx90a():
    with pytest.raises(SystemExit) as e:
        with patch("sys.argv", ["omniperf", "analyze", "--list-metrics", "gfx90a"]):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--list-metrics",
                "gfx90a",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--list-metrics",
                "gfx90a",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.list_metrics
def test_list_metrics_gfx906():
    with pytest.raises(SystemExit) as e:
        with patch("sys.argv", ["omniperf", "analyze", "--list-metrics", "gfx906"]):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--list-metrics",
                "gfx906",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--list-metrics",
                "gfx906",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.list_metrics
def test_list_metrics_gfx908():
    with pytest.raises(SystemExit) as e:
        with patch("sys.argv", ["omniperf", "analyze", "--list-metrics", "gfx908"]):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--list-metrics",
                "gfx908",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--list-metrics",
                "gfx908",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_metrics
def test_filter_metrics_1():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--metric",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--metric",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_metrics
def test_filter_metrics_2():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--metric",
                "5",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--metric",
                "5",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_metrics
def test_filter_metrics_3():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--metric",
                "5.2.2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--metric",
                "5.2.2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_metrics
def test_filter_metrics_4():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--metric",
                "6.1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--metric",
                "6.1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_metrics
def test_filter_metrics_5():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--metric",
                "10",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--metric",
                "10",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_metrics
def test_filter_metrics_6():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--metric",
                "100",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--metric",
                "100",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_kernel
def test_filter_kernel_1():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_kernel
def test_filter_kernel_2():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.filter_kernel
def test_filter_kernel_3():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel",
                "0",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel",
                "0",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.dispatch
def test_dispatch_1():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--dispatch",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--dispatch",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.dispatch
def test_dispatch_2():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--dispatch",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--dispatch",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.dispatch
def test_dispatch_3():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--dispatch",
                "2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--dispatch",
                "2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.dispatch
def test_dispatch_4():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--dispatch",
                "1",
                "4",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--dispatch",
                "1",
                "4",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.dispatch
def test_dispatch_5():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--dispatch",
                "5",
                "6",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--dispatch",
                "5",
                "6",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.misc
def test_gpu_ids():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--gpu-id",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--gpu-id",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.normal_unit
def test_normal_unit_per_wave():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--normal-unit",
                "per_wave",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--normal-unit",
                "per_wave",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.normal_unit
def test_normal_unit_per_cycle():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--normal-unit",
                "per_cycle",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--normal-unit",
                "per_cycle",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.normal_unit
def test_normal_unit_per_second():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--normal-unit",
                "per_second",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--normal-unit",
                "per_second",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.normal_unit
def test_normal_unit_per_kernel():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--normal-unit",
                "per_kernel",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--normal-unit",
                "per_kernel",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.max_kernel
def test_max_kernel_num_1():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--max-kernel-num",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--max-kernel-num",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.max_kernel
def test_max_kernel_num_2():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--max-kernel-num",
                "5",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--max-kernel-num",
                "5",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.max_kernel
def test_max_kernel_num_3():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--max-kernel-num",
                "10",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--max-kernel-num",
                "10",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.max_kernel
def test_max_kernel_num_4():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--max-kernel-num",
                "15",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--max-kernel-num",
                "15",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.time_unit
def test_time_unit_s():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--time-unit",
                "s",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--time-unit",
                "s",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.time_unit
def test_time_unit_ms():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--time-unit",
                "ms",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--time-unit",
                "ms",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.time_unit
def test_time_unit_us():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--time-unit",
                "us",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--time-unit",
                "us",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.time_unit
def test_time_unit_ns():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--time-unit",
                "ns",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--time-unit",
                "ns",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.decimal
def test_decimal_1():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--decimal",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--decimal",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.decimal
def test_decimal_2():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--decimal",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--decimal",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.decimal
def test_decimal_3():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--decimal",
                "4",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--decimal",
                "4",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.misc
def test_save_dfs():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--save-dfs",
                "saved_dfs",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--save-dfs",
                "saved_dfs",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.col
def test_col_1():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--cols",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--cols",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.col
def test_col_2():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--cols",
                "2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--cols",
                "2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.col
def test_col_3():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--cols",
                "0",
                "2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--cols",
                "0",
                "2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.misc
def test_g():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "-g",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "-g",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.kernel_verbose
def test_kernel_verbose_0():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel-verbose",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel-verbose",
                "0",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.kernel_verbose
def test_kernel_verbose_1():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel-verbose",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel-verbose",
                "1",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.kernel_verbose
def test_kernel_verbose_2():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel-verbose",
                "2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel-verbose",
                "2",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.kernel_verbose
def test_kernel_verbose_3():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel-verbose",
                "3",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel-verbose",
                "3",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.kernel_verbose
def test_kernel_verbose_4():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel-verbose",
                "4",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel-verbose",
                "4",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.kernel_verbose
def test_kernel_verbose_5():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel-verbose",
                "5",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel-verbose",
                "5",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.kernel_verbose
def test_kernel_verbose_6():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--kernel-verbose",
                "6",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--kernel-verbose",
                "6",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.misc
def test_baseline():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--path",
                "tests/workloads/mixbench/mi100",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi200",
                "--path",
                "tests/workloads/mixbench1/mi200",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--path",
                "tests/workloads/mixbench1/mi100",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0

@pytest.mark.misc
def test_dependency_mi100():
    with pytest.raises(SystemExit) as e:
        with patch(
            "sys.argv",
            [
                "omniperf",
                "analyze",
                "--path",
                "tests/workloads/mixbench/mi100",
                "--dependency",
            ],
        ):
            omniperf.main()
    assert e.value.code == 0
