from typing import NamedTuple

class Txn(NamedTuple):
    sender : any
    command : str
    def __str__(self):
        return f"{self.sender} : {self.command}"

class VoteInfo(NamedTuple):
    idx : int  # Unique ID 
    roundx : int   # Round of VoteInfo
    parent_id : int
    parent_round : int

class QC(NamedTuple):
    vote_info : VoteInfo 
    author : any = None


class Block(NamedTuple):
    author : any 
    roundx : int
    payload: Txn
    qc: QC
    parent : any
    isCommitted : bool = False
    idx : int = -1    # block_id 
  
class ProposalMsg(NamedTuple):
    block : Block    # Current Block
    last_round_tc : any   # TODO : Implement this
    high_commit_qc : QC = None # QC of Highest Committed Block
  
class VoteMsg(NamedTuple):
    vote_info : VoteInfo
    high_commit_qc : QC
    sender : any

class TimeoutInfo(NamedTuple):
    roundx : int
    high_qc : QC
    sender : any

class TC(NamedTuple):
    roundx : int = None            # All timeout messages that form TC have the same round
    tmo_high_qc_rounds: list = []  # A vector of 2f + 1 high qc round numbers of timeout messages that form TC
    #tmo signatures; // A vector of 2f + 1 validator signatures on (round, respective high qc round)

class TimeoutMsg(NamedTuple):
    tmo_info : TimeoutInfo  # TimeoutInfo for some round with a high qc
    last_round_tc : TC = None     # TC for tmo info.round − 1 if tmo info.high qc.round 6= tmo info.round − 1, else ⊥
    high_commit_qc : QC = None    # QC to synchronize on committed blocks

class pendingTOBlock(NamedTuple):
    senders : set = set()
    roundx : int = 0
    tmo_info : list = []