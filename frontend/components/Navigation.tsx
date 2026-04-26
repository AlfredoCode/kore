import {
  Home,
  Calendar,
  Clock,
  Files,
  Ticket,
  User,
  LogOut,
  Presentation,
  Brain,
} from "lucide-react";
import NavigationButton from "./NavigationButton";

const Navigation = () => {
  return (
    <div className="bg-neutral-950 w-50 flex flex-col h-dvh">
      {/* Scrollable main menu */}
      <div
        className="flex-1 overflow-y-auto pt-3"
        style={{
          scrollbarWidth: "thin", // Firefox
          scrollbarColor: "white transparent", // Firefox thumb / track
        }}
      >
        <NavigationButton title="Dashboard" icon={<Home className="w-4" />} />

        <NavigationButton
          title="Attendance"
          icon={<Clock className="w-4" />}
          subMenu={[
            { title: "Overview" },
            { title: "Absence" },
            { title: "Reports" },
          ]}
          subMenuOpened
        />

        <NavigationButton
          title="Tickets"
          icon={<Ticket className="w-4" />}
          subMenu={[{ title: "All tickets" }, { title: "My tickets" }]}
          subMenuOpened
        />

        <NavigationButton
          title="Project management"
          icon={<Presentation className="w-4" />}
          subMenu={[
            { title: "Sprint" },
            { title: "KPI" },
            { title: "Projects" },
          ]}
        />

        <NavigationButton
          title="Knowledge base / wiki"
          icon={<Brain className="w-4" />}
        />

        <NavigationButton title="Documents" icon={<Files className="w-4" />} />
      </div>

      {/* Bottom section — always visible */}
      <div className="pt-3 border-t border-neutral-700">
        <NavigationButton title="Events" icon={<Calendar className="w-4" />} />

        <NavigationButton
          title="Personal"
          icon={<User className="w-4" />}
          subMenu={[
            { title: "My team" },
            { title: "Financial" },
            { title: "Personal information" },
          ]}
          subMenuOpened
        />

        <NavigationButton
          styles="mt-2 justify-center"
          icon={<LogOut className="w-4 text-red-500" />}
        />
      </div>
    </div>
  );
};

export default Navigation;
