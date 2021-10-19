from Ledger import Ledger
from Block-tree import VoteInfo

class Safety:
    def __init__(self) -> None:
        self.private_key = None # Private Key
        self.public_keys = [] # Public keys of all replicas
        self.highest_vote_round = 0 # Max of round_value voted so far
        self.highest_qc_round = 0 # Max of highQC voted so far

    def increase_highest_vote_round(self, round) -> None:
        """ Commit not to vote in rounds < highest_vote_round
        Args:
            round (int): current round number
        """
        self.highest_vote_round = max(round,self.highest_vote_round)

    def update_highest_qc_round(self, qc_round) -> None:
        """ Update the highest qc round 

        Args:
            qc_round (int): 
        """
        self.highest_qc_round = max(qc_round, self.highest_qc_round)
    
    def consecutive(self, block_round, round) -> bool:
        """
        To check if `block_round` is the next round of `round` or not 

        Args:
            block_round (int): [description]
            round (int): [description]
        Returns:
            bool: True if `block_round` == round + 1 else False
        """
        return round + 1 == block_round
    
    def safe_to_extend(self, block_round, qc_round, tc) -> bool:
        # TODO : Check the type of tc
        """ 
        To check if current tc is safe to extend or not 

        Args:
            block_round (int): [description]
            qc_round (int): [description]
            tc (): [description]
        Returns:
            bool: 
        """
        # Two Conditions 
        # 1. block_round is next round of tc.round
        # 2. qc_round >= max (tc.tmo_high_qc_rounds)
        return self.consecutive(block_round, tc.round) \
            and qc_round >= max(tc.tmo_high_qc_rounds)

    def safe_to_vote(self, block_round, qc_round, tc) -> bool:
        """
        To check if current tc is safe to vote or not

        Args:
            block_round (int): [description]
            qc_round (int): [description]
            tc (): [description]

        Returns:
            bool: [description]
        """
        # Two Conditions 
        # 1. Must vote in monotonically increasing rounds
        # 2. Must extend a smaller round

        if block_round <= max(self.highest_vote_round, qc_round):
            return False

        # Extending QC from previous round || safe to extend due to tc
        return self.consecutive(block_round, qc_round) \
            or self.safe_to_extend(block_round, qc_round, tc)
        
    def safe_to_timeout(self, round, qc_round, tc) -> bool:
        """ 

        Args:
            round (int): [description]
            qc_round (int): [description]
            tc (): [description]
        
        Returns :
            bool : 
        """

        # Respect highest_qc_round and don't timeout for past rounds
        if qc_round < self.highest_qc_round \
            or round < max (self.highest_vote_round-1, qc_round):
                return False
        
        # QC or TC in previous round must allow timeout
        return self.consecutive(round, qc_round) or self.consecutive(round, tc.round)
    
    def commit_state_id_candidate(self, block_round, qc):
        """[summary]

        Args:
            block_round ([type]): [description]
            qc ([type]): [description]
        """
        # Find the committed id in case a qc is formed in the vote round

        if self.consecutive(block_round, qc.vote_info.round):
            return Ledger.pending_state(qc.id)
        else:
            return None 
    
    def make_vote(self, b, last_tc):
        qc_round = b.qc.vote_info.round  # qc_round of block

        if self.valid_signatures(b, last_tc) and self.safe_to_vote(b.round, qc_round, last_tc):
            self.update_highest_qc_round(qc_round)
            self.increase_highest_vote_round(b.round)

            vote_info = VoteInfo((b.id,b.round),(b.qc.vote_info.id, qc_round))
    def valid_signatures(self, b, last_tc):
        # TODO : Implement this : Validate with available Public keys 
        return True