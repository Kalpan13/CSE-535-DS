from typing import NamedTuple

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
    payload: str
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
