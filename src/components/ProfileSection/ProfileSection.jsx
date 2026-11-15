import styles from './ProfileSection.module.css'

export default function ProfileSection({ summary }) {
  return (
    <section className={styles.section}>
      <h2 className={styles.title}>Profile</h2>
      <p className={styles.text}>{summary}</p>
    </section>
  )
}
