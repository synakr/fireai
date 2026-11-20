# QR Print Bridge

QR Print Bridge is a QR-based print-order workflow for a small print shop. Customers scan a shop-specific QR code, upload a document, and choose print preferences. The vendor reviews incoming jobs in a desktop queue and can preview, print, or reject them.

The repository also contains a small Python analysis tool that reads the fieldwork CSV and summarizes observed queue waits and workflow patterns. This analysis module is the assignment's data-driven tool; it runs independently of the live printing application.

## Fieldwork context

- **Person:** Shital Ghosh (printing shop owner / operator)
- **Place:** Coffee House, beside the ECE Department, NIT Agartala
- **Date:** 20 November 2026
- **Dataset:** 25 print-job records in [`data/data.csv`](data/data.csv)
- **Collection:** Direct observation supplemented by details and timestamps from the vendor's existing WhatsApp conversation history because the fieldwork window was limited. See [`assignment-docs/fieldwork.md`](assignment-docs/fieldwork.md) for the collection note and evidence references.

## What the project does

### Guest web app (`guest/`)

- Resolves a vendor from the shop-specific `/v/:slug` link.
- Accepts PDF, JPG, and PNG files up to 25 MB.
- Collects black-and-white or colour, paper size, orientation, single-/double-sided printing, copy count, and optional PDF page ranges.
- Uploads the file to the private Supabase Storage bucket and records the print preferences with the job.

### Vendor desktop app (`vendor-desktop/`)

- Provides vendor sign-in and a shop profile.
- Displays a QR code for the guest upload link.
- Receives cloud print jobs and downloads their files to the local Windows print station.
- Lets the vendor preview, print, or reject queued jobs.
- Sends the selected print preferences to the Windows printing pipeline.

### Fieldwork analysis (`analysis/`)

- Reads the raw CSV using Python's standard library.
- Reports job count, average/median/maximum queue wait, average processing duration, submission methods, and queue-wait comparisons.
- Flags overlapping processing intervals and shows the longest-wait job IDs.

## Repository layout

```text
qr-print-bridge/
├── analysis/
│   ├── analyze_jobs.py          # Reads data.csv and calculates workflow metrics
│   ├── sample-output.txt        # Actual output for the included CSV
│   └── README.md                # Analysis-specific run notes
├── data/
│   └── data.csv                 # 25 fieldwork print-job records
├── guest/                       # Customer-facing React + Vite app
├── vendor-desktop/              # Electron + React vendor application
├── supabase/
│   └── migrations/              # Database, RPC, RLS and Storage setup
├── assignment-docs/
│   ├── research.md               # Problem, existing approaches and sources
│   ├── fieldwork.md              # Observation, conversation and data collection
│   ├── reflection.md             # Self-completion scaffold; must be written by the author
│   └── submission-checklist.md   # Remaining submission formalities
├── evidence/                     # Add the original timestamped fieldwork photos
├── ai-chats/                     # Add exported AI conversations used for this project
├── .env.example
├── package.json
└── README.md
```

## Requirements

- Node.js 20 or newer and npm 10 or newer
- Python 3.8 or newer
- Windows 10/11 for the Electron local printing pipeline
- A Supabase project for authentication, Postgres, Realtime, and private Storage
- A Windows printer installed and configured in Windows

## Setup

### 1. Install dependencies

Run from the repository root:

```bash
npm install
```

### 2. Configure environment variables

Copy `.env.example` to `.env` and fill in your Supabase project URL and anon/publishable key:

```dotenv
VITE_SUPABASE_URL=https://YOUR_PROJECT.supabase.co
VITE_SUPABASE_ANON_KEY=YOUR_SUPABASE_ANON_OR_PUBLISHABLE_KEY
VITE_GUEST_BASE_URL=http://localhost:5174
```

For a phone to open the QR code during local testing, `VITE_GUEST_BASE_URL` must be reachable from that phone. Use a deployed guest URL or a LAN-accessible URL instead of `localhost` when scanning from another device.

Never put a Supabase service-role key in the client-side `.env` file or commit secrets.

### 3. Configure Supabase

Open `supabase/migrations/202611200001_initial_schema.sql` and run it in your Supabase project using the SQL Editor.

The migration creates:

- `vendor_profiles` and `print_jobs`
- The vendor-profile creation trigger
- Guest reservation and upload-completion RPCs
- Row-level security policies
- A private `print-jobs` Storage bucket and upload/read/delete policies
- Realtime publication for `print_jobs`

After applying it, confirm that the `print-jobs` bucket exists and that Realtime is enabled for `print_jobs`.

### 4. Run the guest app

In terminal 1:

```bash
npm run dev:guest
```

The guest app runs at `http://localhost:5174`.

### 5. Run the vendor desktop app

In terminal 2:

```bash
npm run dev:desktop
```

The Electron renderer uses Vite on `http://localhost:5173`. Sign in or create a vendor account, complete the shop profile, and use the generated guest URL/QR code.

### 6. Build and type-check

```bash
npm run typecheck
npm run build
```

The guest and desktop apps build independently into their respective `dist/` directories.

## Run the fieldwork analysis

Run this command from the repository root:

```bash
python analysis/analyze_jobs.py
```

The script reads `data/data.csv` by default. You can also pass another CSV with the same required columns:

```bash
python analysis/analyze_jobs.py path/to/another-data.csv
```

The long-wait threshold is configurable (default: 5 minutes). For example:

```bash
python analysis/analyze_jobs.py --long-wait-threshold 4
```

This makes it easy to demonstrate a live threshold change during the technical call.

Run the automated analysis tests:

```bash
npm test
```

No third-party Python packages are required.

## Actual output for the included dataset

This is the terminal output produced by running `python analysis/analyze_jobs.py` against the included 25-row `data/data.csv`:

```text
PRINT-SHOP WORKFLOW ANALYSIS
==============================
Input file:                    data/data.csv
Total jobs observed:           25
Average queue wait:            4.08 minutes
Median queue wait:             4.00 minutes
Maximum queue wait:            7 minutes
Average processing time:       1.60 minutes
Jobs needing configuration:    15/25
Jobs with vendor interruption: 10/25
Longest-wait job(s):            J019, J022, J025
Long-wait threshold:             5 minutes
Jobs at/above threshold:         9/25
Long-wait job IDs:               J005, J008, J012, J015, J017, J019, J022, J024, J025

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

The output is also saved in [`analysis/sample-output.txt`](analysis/sample-output.txt).

## What the analysis gets wrong / limitations

- **Small sample:** The analysis covers 25 records from one shop and one fieldwork date. It cannot establish typical demand, daily peak periods, or long-term performance.
- **Mixed collection sources:** The fieldwork notes say the CSV combines direct observation with details and timestamps from WhatsApp history. The CSV has no per-row source column, so an individual record cannot currently be traced to its collection source from the CSV alone.
- **Overlapping processing intervals:** The current data produces 21 overlapping pairs of `processing_start`–`processing_end` intervals. If these represent one printer, check the original notes and WhatsApp timestamps. The script flags overlaps; it cannot determine which interpretation is correct.
- **Highly regular timestamps:** Several records have closely spaced, repeated minute-level timestamps. Verify each value against the original observation notes or WhatsApp history before relying on the exact timing comparisons.
- **Queue wait is accepted as recorded:** The script checks that queue-wait values are numeric and non-negative, but does not independently reconstruct them from received and processing-start times.
- **No causal inference:** The comparisons show associations in this small sample. They do not prove that configuration requirements or vendor interruptions caused longer waits.
- **No prediction:** The script is descriptive. It does not forecast queue lengths, predict demand, estimate lost revenue, or automatically allocate staff.
- **Clock-only timestamps:** The CSV stores `HH:MM` values without a date per row. The overlap check assumes one shared observation timeline and is not suitable for combining records from multiple dates without extending the schema.
- **Issue field semantics:** The CSV uses the literal text `None` in some issue cells. The script interprets it as “no issue reported”; verify this interpretation against the source notes.

## Application limitations

- The local Electron printing pipeline currently targets Windows.
- Actual output depends on the installed printer driver and its supported paper sizes, colour, and duplex capabilities. If a requested paper size or duplex mode is unsupported, verify the printer's behaviour before handing the printout to a customer.
- PDF page ranges are passed to Electron's PDF print pipeline. Page-range selection does not apply to image files.
- A successful print status means the operating system accepted the print job; it does not independently verify that physical pages came out correctly.
- The prototype does not implement payments, a live shop-open/closed indicator, or hostel delivery.
- The analysis script and the live application are separate modules; the live app does not ingest the fieldwork CSV.

## Demo recording

---will be attaching the link soon---

## Timeline:

- initialised: 3pm
- first commit (research.md): 3:15pm to 4:30pm
- fieldwork: 4:15 to 5:30pm
- coding: 5:30 to 9:30pm
- finalised: 9:30 to 11:30pm

## Being Frank:

- Eventhough a lot had been goiong on today; including internal exams, one mandatory falicitation event, placements drive, semester minor projects etc; i tried to give my full effort on this project
- there are some gaps in my project, due to time constraints and pre-occupied mind;
- Required a lot of planning from 3pm to now; managing other simultaneous jobs;

THANK YOU
