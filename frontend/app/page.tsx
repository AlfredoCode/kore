import ComponentMounter from "@/components/ComponentMounter";

const Home = () => {
  return (
    <div className="md:h-full xl:h-screen bg-slate-800 flex-1 w-full flex flex-row p-3 gap-3">
      <section title="Helpdesk">
        <ComponentMounter title={"Latest tickets"} width={400} height="full" />
      </section>
      <section title="General" className="w-full flex flex-col gap-3">
        <section title="Attendance" className="flex h-full gap-3">
          <ComponentMounter
            title={"Attendance control"}
            width="full"
            height="full"
          />
          <ComponentMounter
            title={"Latest attendance actions"}
            width={400}
            height="full"
          />
        </section>
        <ComponentMounter title={"Personal"} width="full" height="full" />
      </section>
    </div>
  );
};

export default Home;
