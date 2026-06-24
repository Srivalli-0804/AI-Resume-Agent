import { useEffect, useState } from "react";
import api from "../services/api";
import Navbar from "../components/Navbar";
function Applications() {

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

  return (
    <>
    <Navbar />

    <div className="min-h-screen bg-slate-950 text-white p-10">

      <h1 className="text-4xl font-bold mb-10">
        Applications Dashboard
      </h1>

      <div className="bg-slate-900 rounded-3xl overflow-hidden border border-slate-800">

        <table className="w-full">

          <thead>

            <tr className="bg-slate-800">

              <th className="p-4 text-left">
                Company
              </th>

              <th className="p-4 text-left">
                Role
              </th>

              <th className="p-4 text-left">
                ATS Score
              </th>

              <th className="p-4 text-left">
                Resume File
              </th>

            </tr>

          </thead>

          <tbody>

            {applications.map((app, index) => (

              <tr
                key={index}
                className="border-b border-slate-800"
              >

                <td className="p-4">
                  {app.company}
                </td>

                <td className="p-4">
                  {app.role}
                </td>

                <td className="p-4 text-green-400 font-semibold">
                  {app.ats_score}
                </td>

                <td className="p-4 text-blue-400">
                  {app.resume_file}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
      </>

  );
}

export default Applications;