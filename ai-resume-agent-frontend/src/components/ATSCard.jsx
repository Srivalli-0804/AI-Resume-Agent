function ATSCard({ result }) {

  if (!result) return null;

  const keywordScore =
    result.keyword_ats_score || 0;

  const semanticScore =
    result.semantic_ats_score || 0;

  const projectScore =
    result.project_score || 0;

  const finalScore =
    result.ats_score || 0;

  let matchLabel = "Poor Match";

  if (finalScore >= 80)
    matchLabel = "Excellent Match";
  else if (finalScore >= 60)
    matchLabel = "Good Match";
  else if (finalScore >= 40)
    matchLabel = "Moderate Match";

  return (

    <div className="space-y-6">

      {/* ATS Metrics */}

      <div className="grid md:grid-cols-4 gap-6">

        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

          <h3 className="text-slate-400 mb-2">
            Final ATS
          </h3>

          <p className="text-5xl font-bold text-green-400">
            {finalScore}%
          </p>

        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

          <h3 className="text-slate-400 mb-2">
            Keyword ATS
          </h3>

          <p className="text-5xl font-bold text-blue-400">
            {keywordScore}%
          </p>

        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

          <h3 className="text-slate-400 mb-2">
            Semantic ATS
          </h3>

          <p className="text-5xl font-bold text-purple-400">
            {semanticScore}%
          </p>

        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

          <h3 className="text-slate-400 mb-2">
            Project Match
          </h3>

          <p className="text-5xl font-bold text-orange-400">
            {projectScore}%
          </p>

        </div>

      </div>

      {/* Match Quality */}

      <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

        <h3 className="text-slate-400 mb-2">
          Overall Match Quality
        </h3>

        <p className="text-3xl font-bold text-green-400">
          {matchLabel}
        </p>

      </div>

      {/* Skills Section */}

      <div className="grid md:grid-cols-2 gap-6">

        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

          <h3 className="text-green-400 font-semibold mb-4">
            Matched Skills
          </h3>

          <div className="flex flex-wrap gap-2">

            {result.matched_skills.map(skill => (

              <span
                key={skill}
                className="bg-green-500/20 text-green-400 px-3 py-2 rounded-full"
              >
                {skill}
              </span>

            ))}

          </div>

        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-3xl p-6">

          <h3 className="text-red-400 font-semibold mb-4">
            Missing Skills
          </h3>

          <div className="flex flex-wrap gap-2">

            {result.missing_skills.map(skill => (

              <span
                key={skill}
                className="bg-red-500/20 text-red-400 px-3 py-2 rounded-full"
              >
                {skill}
              </span>

            ))}

          </div>

        </div>

      </div>

    </div>

  );
}

export default ATSCard;