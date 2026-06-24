import { useState } from "react";
import api from "../services/api";

function ResumeCard() {
  const [file, setFile] = useState(null);
  const [uploadStatus, setUploadStatus] = useState("");
  const [resumeId, setResumeId] = useState("");

  const handleUpload = async () => {
    if (!file) {
      alert("Please select a resume");
      return;
    }

    const formData = new FormData();

    formData.append("resume", file);

    try {
      setUploadStatus("Uploading...");

      const response = await api.post(
        "/upload-resume",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResumeId(response.data.resume_id);

      localStorage.setItem(
        "resume_id",
        response.data.resume_id
      );

      setUploadStatus("Resume Uploaded Successfully");
    } catch (error) {
      console.error(error);

      setUploadStatus("Upload Failed");
    }
  };

  return (
    <div className="bg-slate-900 border border-slate-800 rounded-3xl p-8">

      <h2 className="text-2xl font-semibold mb-6">
        Upload Resume
      </h2>

      

      <input
        type="file"
        onChange={(e) => {
        setFile(e.target.files[0]);
          console.log(e.target.files[0]);
        }}
       className="bg-white text-black p-2 rounded"
        />



      
{file && (
  <p className="text-green-400 mb-4">
    Selected: {file.name}
  </p>
)}

      <button
        onClick={handleUpload}
        className="bg-blue-500 hover:bg-blue-600 px-6 py-3 rounded-xl font-semibold"
      >
        Upload Resume
      </button>

      {uploadStatus && (
        <p className="mt-4 text-slate-300">
          {uploadStatus}
        </p>
      )}

      {resumeId && (
        <div className="mt-4 bg-slate-800 p-4 rounded-xl">
          Resume ID:
          <p className="text-blue-400 break-all">
            {resumeId}
          </p>
        </div>
      )}

    </div>
  );
}

export default ResumeCard;