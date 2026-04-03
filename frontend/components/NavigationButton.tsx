"use client";
import React, { useState, useRef, useEffect } from "react";
import { ChevronDown, ChevronRight } from "lucide-react";

interface BaseButtonProps {
  title?: string;
  icon?: React.ReactNode;
  destination?: string;
  styles?: string;
}
interface ButtonWithSubMenuProps extends BaseButtonProps {
  subMenu: NavigationButtonProps[];
  subMenuOpened?: boolean;
}

interface ButtonWithoutSubMenuProps extends BaseButtonProps {
  subMenu?: undefined;
  subMenuOpened?: never;
}

type NavigationButtonProps = ButtonWithSubMenuProps | ButtonWithoutSubMenuProps;

const NavigationButton = (props: NavigationButtonProps) => {
  const { title, icon, styles = "" } = props;
  const subMenu = props.subMenu;

  const subMenuRef = useRef<HTMLDivElement>(null);
  const [maxHeight, setMaxHeight] = useState("0px");

  const hasSubMenu = subMenu?.length ?? 0 > 0;
  const initialOpen =
    hasSubMenu && props.subMenuOpened ? props.subMenuOpened : false;
  const [isOpen, setIsOpen] = useState(initialOpen);

  useEffect(() => {
    if (subMenuRef.current) {
      setMaxHeight(isOpen ? `${subMenuRef.current.scrollHeight}px` : "0px");
    }
  }, [isOpen]);

  return (
    <>
      <div
        className={`text-xs p-2 text-slate-50 select-none hover:cursor-pointer hover:bg-neutral-900 transition-all duration-30 ease-linear flex justify-between items-center ${styles}`}
        onClick={() => hasSubMenu && setIsOpen(!isOpen)}
      >
        <div className="flex items-center gap-2">
          {icon && <span>{icon}</span>}
          {title}
        </div>

        {hasSubMenu && (
          <span>
            {isOpen ? (
              <ChevronDown className="w-4 h-4" />
            ) : (
              <ChevronRight className="w-4 h-4" />
            )}
          </span>
        )}
      </div>

      {hasSubMenu && (
        <div
          ref={subMenuRef}
          style={{ maxHeight }}
          className="ml-4 border-l border-neutral-700 overflow-hidden transition-[max-height] duration-100"
        >
          {subMenu!.map((subButton, index) => (
            <NavigationButton key={index} {...subButton} />
          ))}
        </div>
      )}
    </>
  );
};

export default NavigationButton;
