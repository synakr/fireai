export type Job = {
  id: string;
  originalName: string;
  mimeType: string;
  size: number;
  status: string;
  createdAt: string;
  message: string;
  previewUrl?: string;
  printSettings?: Record<string, unknown>;
};

export type State = {
  host: string;
  port: number;
  guestUrl: string;
  sessionToken: string;
  printers: string[];
  selectedPrinter: string;
  jobs: Job[];
};
