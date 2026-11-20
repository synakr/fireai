/// <reference types="vite/client" />
interface Window {
  printHost: {
    getState: () => Promise<any>;
    hasCloudJob: (id: string) => Promise<boolean>;
    printJob: (id: string) => Promise<{ id: string; status: string; message: string }>;
    rejectJob: (id: string) => Promise<{ id: string; status: string; message: string }>;
    clearCompleted: () => Promise<any>;
    refreshPrinters: () => Promise<any>;
    openQrPreview: (
      qr: string,
      guestUrl: string,
    ) => Promise<{ success: boolean }>;
    queueCloudJob: (
      metadata: {
        jobId: string;
        name: string;
        mimeType: string;
        size: number;
        options: Record<string, unknown>;
      },
      data: ArrayBuffer,
    ) => Promise<any>;
    relayStart: (metadata: {
      jobId: string;
      name: string;
      mimeType: string;
      size: number;
      options: Record<string, unknown>;
    }) => Promise<any>;
    relayChunk: (id: string, chunk: ArrayBuffer) => Promise<void>;
    relayEnd: (id: string) => Promise<any>;
    relayCancel: (id: string) => Promise<void>;
    onRelayResult: (
      callback: (result: {
        jobId: string;
        success: boolean;
        status: string;
        message: string;
      }) => void,
    ) => () => void;
    onChange: (callback: () => void) => () => void;
  };
}
