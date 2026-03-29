import React from "react";

interface ComponentMounterProps {
  width?: number | string | null;
  height?: number | string | null;
  title?: string | null;
  component?: React.ReactNode | null;
}

const ComponentMounter = ({
  title,
  width,
  height,
  component,
}: ComponentMounterProps) => {
  const className = `bg-slate-400 rounded-xl flex items-center justify-center relative flex-col overflow-hidden
    ${typeof width === "string" ? `w-${width}` : "w-auto"}
    ${typeof height === "string" ? `h-${height}` : "h-auto"}`;

  const style: React.CSSProperties = {};
  if (typeof width === "number") style.width = `${width}px`;
  if (typeof height === "number") style.height = `${height}px`;

  return (
    <div className={className} style={style}>
      {component ? (
        <>{component}</>
      ) : (
        <>
          {title && (
            <span className="text-slate-950 font-sans text-[1em] top-[1em] absolute font-bold">
              {title}
            </span>
          )}
          <span className="text-gray-600 font-sans text-[1.25em] uppercase">
            Component Mounter
          </span>
        </>
      )}
    </div>
  );
};

export default ComponentMounter;
