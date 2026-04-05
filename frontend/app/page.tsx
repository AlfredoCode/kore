import ComponentMounter from "@/components/ComponentMounter";

const Home = () => {
  return (
    <div className="h-dvh bg-slate-800 flex-1  flex flex-col xl:flex-row p-3 gap-3 overflow-y-auto">
      <section title="Helpdesk" className="w-full xl:w-1/2 min-h-full order-0">
        <ComponentMounter title="Latest tickets" className="w-full h-full" />
      </section>

      <section
        title="General"
        className="w-full flex flex-col gap-3 min-h-[200%] xl:min-h-auto"
      >
        <section title="Attendance" className="flex h-full gap-3">
          <ComponentMounter
            title="Attendance control"
            className="w-full h-full"
          />

          <ComponentMounter
            title="Latest attendance actions"
            className="w-100 h-full hidden xl:flex"
          />
        </section>

        <ComponentMounter title="Personal" className="w-full h-full" />
      </section>
    </div>
  );
};

export default Home;
