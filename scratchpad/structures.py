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
    def __str__(self):
        return f"{self.idx}"

class QC(NamedTuple):
    vote_info : VoteInfo 
    author : any = None
    def __str__(self):
        return f"{self.vote_info} : {self.author}"

class Block(NamedTuple):
    author : any 
    roundx : int
    payload: Txn
    qc: QC
    parent : any
    isCommitted : bool = False
    idx : int = -1    # block_id 
    def __str__(self):
        return f"{self.idx}"
  
class ProposalMsg(NamedTuple):
    block : Block    # Current Block
    last_round_tc : any   # TODO : Implement this
    high_commit_qc : QC = None # QC of Highest Committed Block
    def __str__(self):
        return f"{self.block} : {self.high_commit_qc}"
  
class VoteMsg(NamedTuple):
    vote_info : VoteInfo
    high_commit_qc : QC
    sender : any
    def __str__(self):
        return f"{self.vote_info} : {self.high_commit_qc}"
