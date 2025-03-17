
let nav = document.getElementById('navbar');


nav.innerHTML = `
<div class="container-fluid ">
      <div class="row d-none d-lg-block d-md-block">
        <nav class="navbar bgcol_pri navbar-expand-sm nav-hide ">
          <div class="container-fluid justify-content-center">
            <ul class="navbar-nav">
              <li class="nav-item">
                <a class="nav-link top-nav-text" aria-current="page" href="https://dbit.in/">DBIT Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link top-nav-text" href="http://parent.dbit.in/"
                  >Parent Login</a
                >
              </li>
              <li class="nav-item">
                <a class="nav-link top-nav-text" href="https://alumni.dbit.in/">Alumni</a>
              </li>
              <li class="nav-item">
                <a class="nav-link top-nav-text" href="https://moodle.dbit.in/">Moodle</a>
              </li>
              <li class="nav-item">
                <a class="nav-link top-nav-text" href="https://elearn.dbit.in/">E-Learn</a>
              </li>
              <li class="nav-item">
                <a class="nav-link top-nav-text" href="http://dbitlrc.dbit.in/">Library</a>
              </li>
              <li class="nav-item">
                <a class="nav-link top-nav-text" href="https://dbcldrive.dbit.in/"
                  >DBCL Drive</a
                >
              </li>
            </ul>
          </div>
        </nav>
      </div>
      <div class="row">
        <img class="p-0" src="/assets/extc_banner.webp" alt="" srcset="" />
      </div>
    </div>

    <header class="sticky-top bgcol_pri" style="z-index: 10">
      <nav
        class="navbar navbar-expand-xl bg-light container-fluid justify-content-between"
      >
        <span class="navbar-brand mb-0 h1 ms-3">EXTC DBIT</span>
        <button
          class="navbar-toggler me-2"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#offcanvasNavbar"
          aria-controls="offcanvasNavbar"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div
          class="offcanvas offcanvas-end"
          tabindex="-1"
          id="offcanvasNavbar"
          aria-labelledby="offcanvasNavbarLabel"
        >
          <div class="offcanvas-header justify-content-end">
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="offcanvas"
              aria-label="Close"
            ></button>
          </div>
          <div class="offcanvas-body">
            <ul class="navbar-nav justify-content-end flex-grow-1 pe-3 offcanvas-nav">
              <li class="nav-item text-center">
                <a class="nav-link active" aria-current="page" href="/index.html">HOME</a>
              </li>
              <li class="nav-item text-center">
                <a class="nav-link" href="/aboutus/aboutus.html">ABOUT US</a>
              </li>
              <li class="nav-item dropdown text-center">
                <a
                  class="nav-link dropdown-toggle"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  ACADEMICS <span class="badge bg-info">New</span>
                </a>
                <ul class="dropdown-menu">
                  <li>
                    <a class="dropdown-item" href="/academics/academic-calendar.html">Academic Calender</a>
                  </li>
                  <li><a class="dropdown-item" href="https://www.dbit.in/timetable.html">Exam Timetable</a></li>
                  <li><a class="dropdown-item" href="/academics/syllabus.html">Syllabus</a></li>
                    <a class="dropdown-item" href="#"
                      >Academic Advisory Board</a
                    >
                  </li>
                  <!-- <li><a class="dropdown-item" href="#">Faculty Profile</a></li> -->
                </ul>
              </li>
              <li class="nav-item dropdown text-center">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  FACULTY
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li class="dropend drop-down">
                <a
                  class="dropdown-item dropdown-toggle"
                  href="#"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                    Profile
                </a>
                <ul class="dropdown-menu sub-menu">
                  <li>
                    <a class="dropdown-item" href="/faculty/faculty_profile.html">Teaching</a>
                  </li>
                  <li>
                    <a class="dropdown-item" href="/faculty/nonteaching.html">Non Teaching</a>
                  </li>
                      </ul>
                  </li>
                  <li><a class="dropdown-item" href="/faculty/faculty_recognition.html">Recognition</a></li>
                  <li class="dropend drop-down">
                    <a
                      class="dropdown-item dropdown-toggle"
                      href="#"
                      role="button"
                      data-bs-toggle="dropdown"
                      aria-expanded="false"
                    >
                      Research
                    </a>
                    <ul class="dropdown-menu sub-menu">
                      <li>
                        <a class="dropdown-item" href="/faculty/research/majorgrants.html">Minor Grants</a>
                      </li>
                      <li>
                      <a class="dropdown-item" href="/faculty/research/minorgrants.html">Major Grants</a>
                    </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <li class="nav-item dropdown text-center">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  STUDENTS
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li>
                    <a class="dropdown-item" href="/assets/pdf/V3_EXTC_ClassTimeTable_AY2022-23_Odd_Semester.pdf">Time Table</a>
                  </li>
                  <li><a class="dropdown-item" href="/students/recognition2.html">Recognition</a></li>
                  <li><a class="dropdown-item" href="/student/sports.html">Sports</a></li>
                </ul>
              </li>
              <li class="nav-item dropdown text-center">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  EXAMINATION
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li>
                    <a class="dropdown-item" href="/students/undergraduateproject.html">Undergraduate Projects</a>
                  </li>
                  <li class="dropend drop-down">
                    <a
                      class="dropdown-item dropdown-toggle"
                      href="#"
                      role="button"
                      data-bs-toggle="dropdown"
                      aria-expanded="false"
                    >
                        Rank Holders
                    </a>
                    <ul class="dropdown-menu sub-menu">
                      <li>
                        <a class="dropdown-item" href="">Internal Assesment</a>
                      </li>
                      <li>
                        <a class="dropdown-item" href="">MU Examination</a>
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              <li class="nav-item dropdown text-center">
              <a
                class="nav-link dropdown-toggle"
                href="#"
                role="button"
                data-bs-toggle="dropdown"
                aria-expanded="false"
              >
                CO-CURRICULAR ACTIVITIES
              </a>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="/cocurricular/newsletter.html">Newsletter</a></li>
                <li><a class="dropdown-item" href="/cocurricular/industrial_training.html">Industrial Visit</a></li>
                <li class="dropend drop-down">
                  <a
                    class="dropdown-item dropdown-toggle"
                    href="#"
                    role="button"
                    data-bs-toggle="dropdown"
                    aria-expanded="false"
                  >
                    Student Chapters
                  </a>
                  <ul class="dropdown-menu sub-menu">
                    <li>
                      <a class="dropdown-item" href="https://ieee.dbit.in/" target="blank">IEEE</a>
                    </li>
                    <li>
                      <a class="dropdown-item" href="https://iete.dbit.in/" target="blank">IETE</a>
                    </li>
                  </ul>
                </li>
                <li><a class="dropdown-item" href="/cocurricular/project.html">Project Exhibition</a></li>
               
              </ul>
            </li>
              <li class="nav-item dropdown text-center">
                <a
                  class="nav-link dropdown-toggle"
                  href="#"
                  id="navbarDropdown"
                  role="button"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  PLACEMENT & INTERNSHIP <span class="badge bg-info">New</span>
                </a>
                <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li>
                    <a
                      class="dropdown-item"
                      href="/placement&internship/intenship.html"
                      >Internship Record</a
                    >
                  </li>
                  <li>
                    <a
                      class="dropdown-item"
                      href="/placement&internship/placement2.html"
                      >Placement Record <span class="badge bg-info">New</span></h1></a
                    >
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </nav>
     

    </header>`
   
