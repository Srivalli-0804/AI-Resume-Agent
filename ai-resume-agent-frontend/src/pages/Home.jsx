import Navbar from "../components/Navbar";
import ResumeCard from "../components/ResumeCard";
import JobInputCard from "../components/JobInputCard";
import ATSCard from "../components/ATSCard";

function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-white">

      <Navbar />

      <section className="max-w-7xl mx-auto px-8 py-24">

        <div className="grid lg:grid-cols-2 gap-16 items-center">

          {/* Left Section */}

          <div>

            <p className="text-blue-400 font-semibold mb-4">
              AI Powered Resume Optimization
            </p>

            <h1 className="text-6xl font-bold leading-tight">

              Generate

              <span className="text-blue-400">
                {" "}ATS Optimized{" "}
              </span>

              Resumes Automatically

            </h1>

            <p className="mt-8 text-slate-400 text-lg">

              Upload your resume and let AI tailor it
              automatically for every company.

            </p>

            <div className="mt-10 flex gap-4">

              <button className="bg-blue-500 hover:bg-blue-600 px-6 py-3 rounded-xl font-semibold">
                Get Started
              </button>

              <button className="border border-slate-700 px-6 py-3 rounded-xl hover:bg-slate-900">
                Learn More
              </button>

            </div>

          </div>

          {/* Right Section */}

            <div className="space-y-6">
              <ResumeCard />
              <JobInputCard />
            </div>

        </div>

      </section>

    </div>
  );
}

export default Home;