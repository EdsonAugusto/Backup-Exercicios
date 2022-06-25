class Miner:

    def __init__(self, stone):
        self.stone = stone
        self.diamond = 0

    def extraction(self):
        while '<' in self.stone and '>' in self.stone:
            self.mining = []
            if '<' in self.stone and '>' in self.stone:
                self.mining.append (self.stone.index ('<'))
                self.mining.append (self.stone.index ('>'))
                if self.mining[0] < self.mining[1]:
                    self.stone = self.stone[:self.mining[0]] + self.stone[self.mining[1] + 1:]
                    self.diamond += 1
                else:
                    self.newStone = self.stone[self.mining[0]:]
                    if '>' in self.newStone:
                        self.mining[1] = self.newStone.index ('>')
                        self.stone = self.stone[:self.mining[0]] + self.stone[self.mining[1] + 1:]
                        self.diamond += 1
                    else:
                        return self.diamond
            else:
                return self.stone, self.diamond
        # else: break


miner = Miner ('<<><>><>><><><><>><<<<>>><><><>>>>><<<<>>')
print (miner.extraction ())