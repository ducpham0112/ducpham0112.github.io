import styles from './SkillsSection.module.css'

export default function SkillsSection({ skills }) {
  return (
    <div className={styles.section}>
      <h2 className={styles.title}>Skills</h2>
      <div className={styles.chips}>
        {skills.map((skill, i) => (
          <span key={i} className={styles.chip}>{skill}</span>
        ))}
      </div>
    </div>
  )
}
