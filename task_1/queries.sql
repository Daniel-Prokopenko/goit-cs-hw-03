--Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
SELECT * 
FROM tasks as t inner join status as s on t.status_id = s.id
WHERE status = 'new'


--Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
SELECT * 
FROM tasks as t inner join status as s on t.status_id = s.id
WHERE name = 'new'


--Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
UPDATE tasks
SET status_id = 2
WHERE id = 3


--Отримати список користувачів, які не мають жодного завдання. Використайте комбінацію SELECT, WHERE NOT IN і підзапит.
SELECT fullname
FROM users
WHERE id NOT IN (
    SELECT DISTINCT user_id
    FROM tasks);


--Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
INSERT into tasks (title, description, status_id, user_id)
VALUES ('new task', 'you need to do this stuff', 1, 3)


--Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
SELECT *
FROM tasks
WHERE status_id != 3


--Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
DELETE from tasks WHERE id = 4


--Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
SELECT *
FROM users
WHERE email LIKE '%org'


--Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
UPDATE users
SET fullname = 'Ronnie Coleman'
WHERE id = 1


--Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
SELECT COUNT(*) 
FROM tasks
GROUP BY status_id


--Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. 
--Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, 
--чия електронна пошта містить певний домен (наприклад, '%@example.com').
SELECT title 
FROM tasks AS t INNER JOIN users AS u ON t.user_id = u.id 
WHERE email LIKE '%@example.com' 


--Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
SELECT title 
FROM tasks 
WHERE description IS NULL


--Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. 
--Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
SELECT fullname, title
FROM tasks as t INNER JOIN users as u on t.user_id = u.id  
WHERE status_id = 2


--Отримати користувачів та кількість їхніх завдань. 
--Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
SELECT fullname, COUNT(title)
FROM tasks as t LEFT JOIN users as u on t.user_id = u.id  
GROUP BY fullname

