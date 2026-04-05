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
    <div className="bg-neutral-950 order-0 pt-3 w-50 flex flex-col h-dvh">
      {/* Dashboard */}
      <NavigationButton title="Dashboard" icon={<Home className="w-4" />} />

      {/* Attendance */}
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

      {/* Tickets */}
      <NavigationButton
        title="Tickets"
        icon={<Ticket className="w-4" />}
        subMenu={[{ title: "All tickets" }, { title: "My tickets" }]}
        subMenuOpened
      />

      {/* Project management */}
      <NavigationButton
        title="Project management"
        icon={<Presentation className="w-4" />}
        subMenu={[{ title: "Sprint" }, { title: "KPI" }, { title: "Projects" }]}
      />

      {/* Knowledge base / wiki */}
      <NavigationButton
        title="Knowledge base / wiki"
        icon={<Brain className="w-4" />}
      />

      {/* Documents */}
      <NavigationButton title="Documents" icon={<Files className="w-4" />} />

      {/* Events */}
      <NavigationButton
        title="Events"
        icon={<Calendar className="w-4" />}
        styles="mt-auto"
      />

      {/* Personal */}
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

      {/* Logout */}
      <NavigationButton
        styles="mt-5 justify-center"
        icon={<LogOut className="w-4 text-red-500" />}
      />
    </div>
  );
};

export default Navigation;
