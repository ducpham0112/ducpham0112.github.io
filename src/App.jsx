import personal from './data/personal.json'
import education from './data/education.json'
import employment from './data/employment.json'
import profile from './data/profile.json'

import Sidebar from './components/Sidebar/Sidebar'
import ProfileSection from './components/ProfileSection/ProfileSection'
import EmploymentTimeline from './components/EmploymentTimeline/EmploymentTimeline'
import Footer from './components/Footer/Footer'
import ThemeToggle from './components/ThemeToggle/ThemeToggle'

import styles from './App.module.css'

function App() {
  return (
    <div className={styles.layout}>
      <Sidebar personal={personal} education={education} />
      <main className={styles.main}>
        <div className={styles.content}>
          <ProfileSection summary={profile.summary} />
          <EmploymentTimeline employment={employment} />
          <Footer />
        </div>
      </main>
      <ThemeToggle />
    </div>
  )
}

export default App
