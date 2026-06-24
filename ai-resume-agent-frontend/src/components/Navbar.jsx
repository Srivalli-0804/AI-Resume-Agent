import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="border-b border-slate-800 bg-slate-950">

      <div className="max-w-7xl mx-auto px-8 py-5 flex items-center justify-between">

        <Link
          to="/"
          className="text-2xl font-bold text-blue-400"
        >
          AI Resume Agent
        </Link>

        <div className="flex gap-8 text-slate-300">

          <Link
            to="/"
            className="hover:text-blue-400"
          >
            Home
          </Link>

          <Link
            to="/applications"
            className="hover:text-blue-400"
          >
            Applications
          </Link>

          <Link
            to="/analytics"
            className="hover:text-blue-400"
          >
            Analytics
          </Link>

          <Link
            to="/recommendations"
            className="hover:text-blue-400"
          >
            Recommendations
          </Link>

        </div>

      </div>

    </nav>
  );
}

export default Navbar;