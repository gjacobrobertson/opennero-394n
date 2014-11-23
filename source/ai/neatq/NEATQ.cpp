#include "core/Common.h"
#include "game/SimEntity.h"
#include "game/SimContext.h"
#include "game/Kernel.h"
#include "ai/AIObject.h"
#include "ai/AgentBrain.h"
#include "ai/rtneat/rtNEAT.h"
#include "ai/neatq/NEATQ.h"
#include "rtneat/population.h"
#include "rtneat/network.h"
#include "scripting/scriptIncludes.h"
#include "math/Random.h"
#include <ostream>
#include <fstream>

namespace OpenNero
{

    void NEATQ::ProcessTick( float32_t incAmt )
    {
        // Increment the spawn tick and evolution tick counters
        ++mSpawnTickCount;
        ++mEvolutionTickCount;

        if (mEvolutionEnabled) {
            tallyAll();
            // Evaluate all brains' scores
            evaluateAll();
        }

        //TODO: backpropagation using TD methods

        // If the total number of units spawned so far exceeds the threshold value AND enough
        // ticks have passed since the last evolution, then a new evolution may commence.
        if (mEvolutionEnabled
            && mTotalUnitsDeleted >= mUnitsToDeleteBeforeFirstJudgment
            && mEvolutionTickCount >= mTimeBetweenEvolutions)
        {
            //Judgment day!
            evolveAll();
            mEvolutionTickCount = 0;
        }
    }


}
