import { Home, Calendar, Ticket, User, LogOut } from "lucide-react";
import NavigationButton from "./NavigationButton";

const Navigation = () => {
  return (
    <div className="bg-neutral-950 md:order-2 xl:order-0 self-end md:w-full md:pt-3 xl:h-screen xl:w-50 flex flex-col">
      <NavigationButton title="Dashboard" icon={<Home className="w-4" />} />
      <NavigationButton
        title="Attendance"
        icon={<Calendar className="w-4" />}
        subMenu={[{ title: "Overview" }, { title: "Reports" }]}
        subMenuOpened
      />
      <NavigationButton
        title="Tickets"
        icon={<Ticket className="w-4" />}
        subMenu={[{ title: "All tickets" }, { title: "My tickets" }]}
        subMenuOpened
      />
      <NavigationButton
        title="Personal"
        icon={<User className="w-4" />}
        subMenu={[
          { title: "My team" },
          { title: "Financial" },
          { title: "Personal information" },
        ]}
      />
      <NavigationButton
        styles="mt-auto justify-center"
        icon={<LogOut className="w-4 text-red-500" />}
      />
    </div>
  );
};

export default Navigation;
