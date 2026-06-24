import { useState } from "react";
import api from "../services/api";
import ATSCard from "./ATSCard";

function JobInputCard() {
  const [jobUrl, setJobUrl] = useState("");
  const [jobDescription, setJobDescription] = useState("");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleProcessJob = async () => {
    const resumeId = localStorage.getItem("resume_id");

    if (!resumeId) {
      alert("Upload resume first");
      return;
    }

    try {
      setLoading(true);

      const response = await api.post(
        "/process-job",
        {
          resume_id: resumeId,
          job_url: jobUrl,
          job_description: jobDescription
        }
      );

      setResult(response.data);
      console.log(response.data);

    } catch (error) {
      console.error(error);
      alert("Job processing failed");
    }

    setLoading(false);
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-8">

      <h2 className="text-2xl font-semibold mb-6">
        Job Details
      </h2>

      <input
        type="text"
        placeholder="LinkedIn Job URL"
        value={jobUrl}
        onChange={(e) => setJobUrl(e.target.value)}
        className="w-full p-3 rounded-xl bg-slate-800 mb-4 text-white"
      />

      <textarea
        rows="8"
        placeholder="Paste Job Description"
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
        className="w-full p-3 rounded-xl bg-slate-800 mb-4 text-white"
      />

      <button
        onClick={handleProcessJob}
        className="bg-blue-500 hover:bg-blue-600 px-6 py-3 rounded-xl font-semibold"
      >
        {loading ? "Processing..." : "Analyze Job"}
      </button>

      {result && (
        <div className="mt-8">
          <ATSCard result={result} />

          <div className="mt-6 bg-slate-800 p-5 rounded-2xl">
            <h3 className="text-lg font-semibold mb-3">
              Recommendations
            </h3>

            <ul className="space-y-2">
              {result.recommendations?.map((item, index) => (
                <li key={index}>
                  💡 {item}
                </li>
              ))}
            </ul>
          </div>

          <div className="mt-6 bg-slate-800 p-5 rounded-2xl">
            <h3 className="text-lg font-semibold mb-3">
              Generated Resume
            </h3>

            <p className="text-blue-400 break-all">
              {result.generated_resume}
            </p>
          </div>

          <div className="mt-6 bg-slate-800 p-5 rounded-2xl">
            <h3 className="text-lg font-semibold mb-3">
              Application ID
            </h3>

            <p className="text-green-400 break-all">
              {result.application_id}
            </p>
          </div>

        </div>
      )}

    </div>
  );
}

export default JobInputCard;