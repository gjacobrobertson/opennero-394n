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
    public:
    	/// Called every step by the OpenNERO system
    	virtual void ProcessTick( float32_t incAmt );
    };

}

#endif /* _OPENNERO_AI_NEATQ_H_ */
