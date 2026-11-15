import Avatar from '../Avatar/Avatar'
import ContactList from '../ContactList/ContactList'
import EducationSection from '../EducationSection/EducationSection'
import SkillsSection from '../SkillsSection/SkillsSection'
import skillsData from '../../data/skills.json'
import styles from './Sidebar.module.css'

const printContacts = (contacts) => contacts.filter(c => c.type === 'email' || c.type === 'linkedin')

export default function Sidebar({ personal, education }) {
  return (
    <aside className={styles.sidebar}>
      {/* Screen layout: top section with avatar + identity */}
      <div className={styles.top}>
        <Avatar />
        <div className={styles.identity}>
          <h1 className={styles.name}>{personal.name}</h1>
          <p className={styles.title}>{personal.title}</p>
        </div>
      </div>
      {/* Print-only header: name/title left, contacts right */}
      <div className={styles.printHeader}>
        <div className={styles.printIdentity}>
          <h1 className={styles.name}>{personal.name}</h1>
          <p className={styles.title}>{personal.title}</p>
        </div>
        <div className={styles.printContacts}>
          <ContactList contacts={printContacts(personal.contacts)} />
        </div>
      </div>
      <div className={styles.divider} />
      <div className={styles.screenContacts}>
        <ContactList contacts={personal.contacts} />
      </div>
      <div className={styles.divider} />
      <div className={styles.printBody}>
        <EducationSection education={education} />
        <div className={styles.divider} />
        <SkillsSection skills={skillsData.skills} />
      </div>
    </aside>
  )
}
