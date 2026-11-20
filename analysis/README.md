# QR Print Bridge — Print-Shop Workflow Analysis

This standalone Python script reads the observed print-job records in `data/data.csv` and produces a summary of the shop's workload, queue waits, submission methods, and recorded issues. It is a small fieldwork-analysis utility alongside QR Print Bridge; it does not connect to or control the printing application.

## Requirements

- Python 3.8 or newer
- No third-party packages are required (the script uses the Python standard library)

## How to run

1. Open a terminal in the repository root (the directory containing `analysis/` and `data/`).
2. Run:

   ```bash
   python analysis/analyze_jobs.py
   ```

   On systems where Python 3 is invoked as `python3`, use:

   ```bash
   python3 analysis/analyze_jobs.py
   ```

The script reads `data/data.csv` by default and prints the report in the terminal. To analyze a different CSV with the same required columns, pass its path:

```bash
python analysis/analyze_jobs.py path/to/another-data.csv
```

The input CSV must contain these columns: `job_id`, `time_received`, `submission_method`, `pages`, `copies`, `print_type`, `configuration_required`, `processing_start`, `processing_end`, `queue_wait_minutes`, `vendor_interrupted`, and `issue`.

## Actual output from the included data

The following is the terminal output produced by running `python analysis/analyze_jobs.py` against the included `data/data.csv` (25 records):

```text
PRINT-SHOP WORKFLOW ANALYSIS
==============================
Input file:                 data\data.csv
Total jobs observed:        25
Average queue wait:         4.08 minutes
Median queue wait:          4.00 minutes
Maximum queue wait:         7 minutes
Average processing time:    1.60 minutes
Jobs needing configuration: 15/25
Jobs with vendor interruption: 10/25

SUBMISSION METHODS
  Walk-in: 10
  WhatsApp: 15

QUEUE WAIT BY CONFIGURATION
Category                  Jobs    Avg wait    Max wait
------------------------------------------------------
No                          10        2.7m          4m
Yes                         15        5.0m          7m

QUEUE WAIT BY VENDOR INTERRUPTION
Category                  Jobs    Avg wait    Max wait
------------------------------------------------------
No                          15        3.3m          7m
Yes                         10        5.3m          7m

QUEUE WAIT BY PRINT TYPE
Category                  Jobs    Avg wait    Max wait
------------------------------------------------------
B&W                         17        3.2m          6m
Colour                       8        5.9m          7m

RECORDED ISSUES
  No issue reported: 10
  Page selection: 3
  Colour settings: 3
  Selected pages: 2
  Print clarification: 2
  Copy count: 2
  Customer clarification: 1
  Paper settings: 1
  Large document: 1

DATA QUALITY CHECK
  Rows with blank issue field: 0
  Overlapping processing-interval pairs: 21
  Review these timestamps if all jobs are expected to use one printer.

INTERPRETATION
  Jobs marked as requiring configuration waited 5.0 min on average, vs 2.7 min for jobs not requiring it.
  Jobs marked with vendor interruption waited 5.3 min on average, vs 3.3 min without interruption.
  These are observed associations, not proof of causation.
```

## What this tool gets wrong / limitations

- **Small, short observation:** The report covers only 25 jobs from one observation session at one shop. It cannot establish typical daily demand, peak periods across days, or long-term performance.
- **Overlapping processing intervals:** The script detects 21 pairs of overlapping `processing_start`–`processing_end` intervals. If these timestamps are intended to represent use of a single printer, they need to be checked against the original notes. The script flags the overlap but cannot determine which timestamp or interpretation is correct.
- **No causal conclusions:** The comparisons show that jobs marked as requiring configuration or vendor interruption had different average queue waits in this sample. They do not prove that either factor caused the longer waits; job size, workload, customer clarifications, or other factors may also matter.
- **Recorded categories are taken at face value:** The script groups values such as `Yes`, `No`, `B&W`, and `Colour` as written. Unexpected spelling or inconsistent labels can split one real category into multiple groups.
- **Queue wait is accepted as recorded:** The script checks that queue-wait values are numeric and non-negative, but it does not independently reconstruct or verify them from `time_received` and `processing_start`.
- **Limited time handling:** Times are parsed as clock times (`HH:MM`) without dates or time zones. Duration calculation handles a job crossing midnight, but the overlap check assumes all records belong to the same observation timeline and does not account for dates.
- **Descriptive, not predictive:** It summarizes the supplied records only. It does not forecast queues, recommend staffing levels, estimate revenue loss, or automatically manage print jobs.

The report should therefore be treated as a descriptive summary to help the vendor discuss workflow bottlenecks, not as a statistically representative or causal study.
