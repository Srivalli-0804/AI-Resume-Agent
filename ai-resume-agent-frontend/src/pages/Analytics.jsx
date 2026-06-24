import { useEffect, useState } from "react";
import Navbar from "../components/Navbar";
import api from "../services/api";

function Analytics() {

  const [applications, setApplications] = useState([]);

  useEffect(() => {
    fetchApplications();
  }, []);

  const fetchApplications = async () => {

    try {

      const response =
        await api.get("/applications");

      setApplications(response.data);

    } catch (error) {

      console.error(error);

    }
  };

  const totalApplications =
    applications.length;

  const averageATS =
    applications.length > 0
      ? (
          applications.reduce(
            (sum, app) => sum + app.ats_score,
            0
          ) / applications.length
        ).toFixed(1)
      : 0;

  const highestATS =
    applications.length > 0
      ? Math.max(
          ...applications.map(
            app => app.ats_score
          )
        )
      : 0;

  const companiesApplied =
    new Set(
      applications.map(
        app => app.company
      )
    ).size;

  return (
    <>
      <Navbar />

      <div className="min-h-screen bg-slate-950 text-white p-10">

        <h1 className="text-4xl font-bold mb-10">
          Analytics Dashboard
        </h1>

        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">

          <div className="bg-slate-900 p-6 rounded-3xl border border-slate-800">
            <h3 className="text-slate-400">
              Total Applications
            </h3>

            <p className="text-5xl font-bold mt-4">
              {totalApplications}
            </p>
          </div>

          <div className="bg-slate-900 p-6 rounded-3xl border border-slate-800">
            <h3 className="text-slate-400">
              Average ATS
            </h3>

            <p className="text-5xl font-bold text-green-400 mt-4">
              {averageATS}
            </p>
          </div>

          <div className="bg-slate-900 p-6 rounded-3xl border border-slate-800">
            <h3 className="text-slate-400">
              Highest ATS
            </h3>

            <p className="text-5xl font-bold text-blue-400 mt-4">
              {highestATS}
            </p>
          </div>

          <div className="bg-slate-900 p-6 rounded-3xl border border-slate-800">
            <h3 className="text-slate-400">
              Companies Applied
            </h3>

            <p className="text-5xl font-bold text-purple-400 mt-4">
              {companiesApplied}
            </p>
          </div>

        </div>

      </div>
    </>
  );
}

export default Analytics;