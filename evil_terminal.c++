#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <curl/curl.h>
#include <csignal>

using namespace std;

bool running = true;

size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

string shortenURL(const string& longUrl) {
    CURL* curl;
    CURLcode res;
    string readBuffer;
    string requestUrl = "http://tinyurl.com/api-create.php?url=" + longUrl;

    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, requestUrl.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
    }
    return readBuffer;
}

string generateSessionID(int length = 12) {
    string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    string result;
    srand(time(0));
    for (int i = 0; i < length; i++) {
        result += chars[rand() % chars.size()];
    }
    return result;
}

void saveHistory(const string& longUrl, const string& shortUrl) {
    ofstream file("link_history.txt", ios::app);
    if (file.is_open()) {
        time_t now = time(0);
        file << "[" << ctime(&now) << "] " << longUrl << " -> " << shortUrl << "\n";
        file.close();
    }
}

void viewHistory() {
    ifstream file("link_history.txt");
    string line;
    if (file.is_open()) {
        cout << "\n===== Link History =====\n";
        while (getline(file, line)) {
            cout << line << endl;
        }
        cout << "========================\n";
        file.close();
    } else {
        cout << "No history found.\n";
    }
}

void clearHistory() {
    ofstream file("link_history.txt", ios::trunc);
    file.close();
    cout << "History cleared successfully.\n";
}

void banner() {
    cout << R"(
             .           .           
             M.          .M          
              MMMMMMMMMMM.           
           .MMM\MMMMMMM/MMM.         
          .MMM.7MMMMMMM.7MMM.        
         .MMMMMMMMMMMMMMMMMMM        
         MMMMMMM.......MMMMMMM       
         MMMMMMMMMMMMMMMMMMMMM       
    MMMM MMMMMMMMMMMMMMMMMMMMM MMMM  
   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD 
   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD 
    MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM  
         MMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMM
         MMMMMMMMMMMMMMMMMMMMM
             MMMMM.  MMMMM
             MMMMM.  MMMMM
             MMMMM   MMMMM  v3.0     
             .MMM.   .MMM.           
          TinyURL GPT - Evil Terminal
============================================================
)" << endl;
}

void menu() {
    cout << "[1] Shorten a URL\n";
    cout << "[2] Generate random session ID\n";
    cout << "[3] View history\n";
    cout << "[4] Clear history\n";
    cout << "[5] Exit\n";
    cout << "============================================================\n";
}

void signalHandler(int signum) {
    cout << "\nCaught Ctrl+C (signal " << signum << "). Exiting safely..." << endl;
    running = false;
}

int main() {
    signal(SIGINT, signalHandler);

    int choice;
    string url, shortUrl;

    banner();
    menu();

    while (running) {
        cout << "Enter choice: ";
        cin >> choice;

        if (!running) break;

        if (choice == 1) {
            cout << "Enter URL: ";
            cin >> url;
            shortUrl = shortenURL(url);
            cout << "Shortened URL: " << shortUrl << endl;
            saveHistory(url, shortUrl);
        }
        else if (choice == 2) {
            cout << "Session ID: " << generateSessionID() << endl;
        }
        else if (choice == 3) {
            viewHistory();
        }
        else if (choice == 4) {
            clearHistory();
        }
        else if (choice == 5) {
            cout << "Goodbye!" << endl;
            break;
        }
        else {
            cout << "Invalid choice!" << endl;
        }
    }
    return 0;
}
