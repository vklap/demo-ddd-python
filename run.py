from app import app, init_db


if __name__ == '__main__':
    from app.domain.entry import Entry
    from app.infrastructure.repositories import entries as entries_repo

    init_db()
    entry1 = Entry(title='Domain Driven Design', text='Tackling complexity in the Heart of Software. The software development community widely acknowledges that domain modeling is central to software design. Through domain models, software developers are able to express rich functionality and translate it into a software implementation that truly serves the needs of its users. But despite its obvious importance, there are few practical resources that explain how to incorporate effective domain modeling into the software development process.')
    entry2 = Entry(title='Design Patterns: Elements of Reusable Object-Oriented Software', text="Design Patterns is a modern classic in the literature of object-oriented development, offering timeless and elegant solutions to common problems in software design. It describes patterns for managing object creation, composing objects into larger structures, and coordinating control flow between objects. The book provides numerous examples where using composition rather than inheritance can improve the reusability and flexibility of code. Note, though, that it's not a tutorial but a catalog that you can use to find an object-oriented design pattern that's appropriate for the needs of your particular application--a selection for virtuoso programmers who appreciate (or require) consistent, well-engineered object-oriented designs.")

    entries_repo.add_entry(entry1)
    entries_repo.add_entry(entry2)

    app.run(debug=True)