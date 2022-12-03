#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include<map>
#include<vector>

using namespace std;
map<string,string> moves{{"A","Rock"},{"B","Paper"},{"C","Scissors"}};
map<string,string> outcome{{"X","lose"},{"Y","draw"},{"Z","win"}}; 
map<string,int> scores{{"Rock",1},{"Paper",2},{"Scissors",3}};
map<string,string> wins{{"Rock","Scissors"},{"Scissors","Paper"},{"Paper","Rock"}}; 
map<string,string> loss{{"Rock","Paper"},{"Scissors","Rock"},{"Paper","Scissors"}}; 



int score(string Player, string Opponent){
    if(Player == Opponent){ //Same move played so draw
        return 3 + scores[Player];
    }
    else if (Opponent == wins[Player]) // The opponent beats the player
    {
        return 6 + scores[Player];
    }
    else { //Look you won 
        return 0 + scores[Player];
    }
}

vector<string> split(string input_string, char delim){
    vector<string> out;
    stringstream ss(input_string);
    string s;
    while (getline(ss,s,delim))
    {
        out.push_back(s);
    }
    return out;  
}

string player_move(string outcome,string opponent){
    if (outcome == "draw"){
        return opponent;
    }else if (outcome == "win")
    {
        return loss[opponent];
    }
    else{
        return wins[opponent];
    }
    
}

int play_game(string fpath){
    ifstream Game_File(fpath);
    int total_score = 0; 
    string Match; 
    while (getline(Game_File,Match))
    {
       vector<string> Moves = split(Match,' ');
       string Opponent = moves[Moves[0]];
       string Player = player_move(outcome[Moves[1]],Opponent);
       int Game_Score = score(Player,Opponent);
       total_score += Game_Score;
    }
    return total_score;    
}

int  main() {
   int Result = play_game("Game.txt"); 
   cout << Result << endl;
   return 0;
}
