class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> check = new HashSet<>();

        for(int i=0;i<9;i++) {
            check.clear();
            for(int j=0;j<9;j++) {
                char ch = board[i][j];
                if(ch == '.')
                continue;
                if(ch < '1' || ch > '9')
                return false;
                if(!check.add(ch))
                return false;
            }
        }

        for(int i=0;i<9;i++) {
            check.clear();
            for(int j=0;j<9;j++) {
                char ch = board[j][i];
                if(ch == '.')
                continue;
                if(ch < '1' || ch > '9')
                return false;
                if(!check.add(ch))
                return false;
            }
        }

        for(int br=0;br<9;br+=3) {
            for(int bc=0;bc<9;bc+=3) {
                check.clear();
                for(int i=br;i<br+3;i++) {
                    for(int j=bc;j<bc+3;j++) {
                        char ch = board[i][j];
                        if(ch == '.')
                        continue;
                        if(ch < '1' || ch > '9')
                        return false;
                        if(!check.add(ch))
                        return false;
                    }
                }
            }
        }
        return true;
    }
}