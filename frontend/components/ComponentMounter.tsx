import React from "react";

interface ComponentMounterProps {
  title?: string | null;
  component?: React.ReactNode | null;
  className?: string; // 👈 add this
}

const ComponentMounter = ({
  title,
  component,
  className = "",
}: ComponentMounterProps) => {
  const baseClasses =
    "bg-slate-400 rounded-xl flex items-center justify-center relative flex-col overflow-hidden shadow-[0_0_5px_1px_black]";

  return (
    <div className={`${baseClasses} ${className}`}>
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
