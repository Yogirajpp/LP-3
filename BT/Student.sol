// SPDX-License-Identifier: GPL-3.0
pragma solidity >=0.8.2 <0.9.0;

contract Student_management {

    struct Student {
        int stud_id;
        string Name;
        string Department;
    }

    Student[] Students;

    // Add a student
    function add_stud(int stud_id, string memory Name, string memory Department) public {
        Student memory stud = Student(stud_id, Name, Department);
        Students.push(stud);
    }

    // Retrieve student by ID
    function getStudent(int stud_id) public view returns (string memory, string memory) {
        for (uint i = 0; i < Students.length; i++) {
            Student memory stud = Students[i];
            if (stud.stud_id == stud_id) {
                return (stud.Name, stud.Department);
            }
        }
        return ("Name Not Found", "Department Not Found");
    }

    // Receive function to handle incoming ether with no data
    receive() external payable {
        // When ether is sent to the contract without data, add a default student
        Students.push(Student(7, "Default Student", "Unknown"));
        emit StudentAdded(7, "Default Student", "Unknown");
    }

    // Fallback Function to handle calls with data or when ether is sent with data
    fallback() external payable {
        // When fallback is triggered, add a default student
        Students.push(Student(7, "Default Student", "Unknown"));
        emit StudentAdded(7, "Default Student", "Unknown");
    }

    // Optional event for logging when a student is added
    event StudentAdded(int stud_id, string Name, string Department);
}
