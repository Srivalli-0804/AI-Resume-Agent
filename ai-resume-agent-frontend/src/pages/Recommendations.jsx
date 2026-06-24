import Navbar from "../components/Navbar";
import { useEffect, useState } from "react";
import api from "../services/api";

function Recommendations() {

  const [recommendations, setRecommendations] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  useEffect(() => {

    const fetchRecommendations =
      async () => {

        const resumeId =
          localStorage.getItem(
            "resume_id"
          );

        if (!resumeId) {

          setLoading(false);
          return;
        }

        try {

          const response =
            await api.get(
              `/recommend-jobs/${resumeId}`
            );

          setRecommendations(
            response.data.recommendations
          );

        } catch (error) {

          console.error(error);

        }

        setLoading(false);
      };

    fetchRecommendations();

  }, []);

  return (

    <div className="min-h-screen bg-[#020817] text-white p-10">

      <h1 className="text-5xl font-bold mb-10">

        Job Recommendations

      </h1>

      {loading ? (

        <p>Loading...</p>

      ) : (

        <div className="grid md:grid-cols-2 gap-6">

          {recommendations.map((job) => (

            <div
              key={job.role}
              className="bg-slate-900 border border-slate-800 rounded-3xl p-6"
            >

              <h2 className="text-2xl font-bold mb-4">

                {job.role}

              </h2>

              <p className="text-slate-400">

                Match Score

              </p>

              <p className="text-4xl font-bold text-green-400">

                {job.match_score}%

              </p>

            </div>

          ))}

        </div>

      )}

    </div>

  );
}

export default Recommendations;