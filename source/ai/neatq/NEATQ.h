/// @file
/// A Python interface for the rtNEAT learning algorithm.

#ifndef _OPENNERO_AI_NEATQ_H_
#define _OPENNERO_AI_NEATQ_H_

#include "core/Preprocessor.h"
#include "rtneat/population.h"
#include "scripting/scripting.h"
#include "ai/AI.h"
#include "ai/Environment.h"
#include "ai/rtneat/ScoreHelper.h"
#include "ai/rtneat/rtNEAT.h"
#include <string>
#include <set>
#include <queue>
#include <iostream>
#include <boost/python.hpp>
#include <boost/bimap.hpp>


namespace OpenNero
{
    using namespace NEAT;
    using namespace std;
    namespace py = boost::python;

    /// @cond
    BOOST_SHARED_DECL(NEATQ);
    /// @endcond

    /// An interface for the RTNEAT learning algorithm
    class NEATQ : public RTNEAT {

	private:

        /// tally the rewards of all the fielded agents
        void tallyAll();

		/// evaluate all brains by compiling their stats
		void evaluateAll();

		/// evolution step that potentially replaces an organism with an
		/// offspring
		void evolveAll();

		/// Delete the unit which is currently associated with the specified
		/// brain and move the brain back to waiting list.
		void deleteUnit(PyOrganismPtr brain);
    };

}

#endif /* _OPENNERO_AI_NEATQ_H_ */
