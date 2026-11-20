import { Printer, RefreshCw } from "lucide-react";
import type { State } from "./types";

type SettingsPanelProps = {
  state: State;
  pending: number;
  done: number;
  onRefreshPrinters: () => void;
};

export function SettingsPanel({
  state,
  pending,
  done,
  onRefreshPrinters,
}: SettingsPanelProps) {
  return (
    <article className="rounded-[19px] border border-[#e7ebf1] bg-white p-[23px_25px] shadow-[0_3px_14px_rgba(24,34,48,0.025)]">
      <div className="mb-[22px] flex items-center justify-between">
        <div className="flex items-center gap-2.5">
          <span className="rounded-[7px] bg-[#e6f8f2] px-[7px] py-1.5 text-[10px] font-extrabold text-[#079879]">02</span>
          <h2 className="font-[Manrope,sans-serif] text-base font-extrabold tracking-[-0.3px]">Print station</h2>
        </div>
        <button
          className="flex items-center gap-1.5 border-0 bg-transparent p-[7px] text-[11px] font-semibold text-[#687587]"
          onClick={onRefreshPrinters}
          type="button"
        >
          <RefreshCw size={14} /> Refresh
        </button>
      </div>

      <label className="mb-2 block text-[9px] font-extrabold tracking-[1.3px] text-[#7c8998]" htmlFor="printer">
        CONNECTED PRINTER
      </label>
      <div className="flex h-[45px] items-center gap-[9px] rounded-[10px] border border-[#e4e9ef] px-3 text-[#687587]">
        <Printer className="text-[#15987c]" size={17} />
        <span id="printer" className="truncate text-xs">
          {state.selectedPrinter || "No printer detected"}
        </span>
      </div>
      <p className="mt-2 min-h-[14px] text-[10px] text-[#8993a1]">
        {state.selectedPrinter
          ? "Using the Windows default printer. Confirm the printer's paper and duplex capabilities before printing."
          : "No default printer detected. Set one in Windows Settings, then refresh."}
      </p>

      <div className="mt-[19px] grid grid-cols-3 border-t border-[#edf0f4] pt-[17px]">
        <div className="flex flex-col gap-[5px]">
          <span className="font-[Manrope,sans-serif] text-[23px] font-extrabold tracking-[-0.8px]">{state.jobs.length}</span>
          <span className="text-[8px] font-extrabold tracking-[1px] text-[#8b95a2]">TOTAL JOBS</span>
        </div>
        <div className="flex flex-col gap-[5px]">
          <span className="font-[Manrope,sans-serif] text-[23px] font-extrabold tracking-[-0.8px] text-[#c78319]">{pending}</span>
          <span className="text-[8px] font-extrabold tracking-[1px] text-[#8b95a2]">TO REVIEW</span>
        </div>
        <div className="flex flex-col gap-[5px]">
          <span className="font-[Manrope,sans-serif] text-[23px] font-extrabold tracking-[-0.8px]">{done}</span>
          <span className="text-[8px] font-extrabold tracking-[1px] text-[#8b95a2]">FINISHED</span>
        </div>
      </div>
    </article>
  );
}
